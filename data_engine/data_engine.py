import asyncio
import websockets
import json
import time
import configs.constants as configs

class DataEngine:
    """ Data engine class """
    def __init__(self) -> None:
         # country wise actions
        self.country_wise_action = {}
        # terding users
        self.contributing_users = {}
        # creations
        self.create = 0
        # number of edits
        self.edits = 0
        # number of inserts
        self.inserts = 0
        # number of deletes
        self.deletes = 0
        # bot actions
        self.bot_actions = 0
        # patrolled/unpatrolled edits
        self.patrolled_edits = 0
        self.unpatrolled_edits = 0
        self.total_actions = 0
    
    async def start_analysis(self,runtime:float) -> None:
        """
        hatnote event collector, this will collect and parse data for a given time period
        """
        async with websockets.connect(configs.WIKI_EVENT_ENDPOINT) as ws:
            now = time.time()
            while ( time.time() - now ) < runtime:
                event = await ws.recv()
                self.total_actions += 1
                print(event)
                json_data = json.loads(event)
                try:
                    if json_data["is_bot"] == True:
                        self.bot_actions += 1
                    
                    if json_data["is_unpatrolled"] == False:
                        self.patrolled_edits += 1
                    else:
                        self.unpatrolled_edits += 1

                    if json_data["action"] == "edit":
                        self.edits += 1
                    elif json_data["action"] == "delete":
                        self.deletes += 1
                    elif json_data["action"] == "insert":
                        self.inserts += 1
                    elif json_data["action"] == "create":
                        self.create += 1
                    
                    if self.contributing_users.get(json_data["user"]) is not None:
                        self.contributing_users[json_data["user"]] += 1
                    else:
                        self.contributing_users[json_data["user"]] = 1

                    if self.country_wise_action.get(json_data["geo_ip"]["country_name"]) is not None:
                        self.country_wise_action[json_data["geo_ip"]["country_name"]] += 1
                    else:
                        self.country_wise_action[json_data["geo_ip"]["country_name"]] = 1
                except Exception as ex:
                    print(ex)
                    continue
            
           