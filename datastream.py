import asyncio
import data_engine.data_engine as analyser
import matplotlib.pyplot as plt

if __name__ == "__main__": 
    runtime = name = input("How long you want to run this script for(please enter in seconds): ") 
    engine = analyser.DataEngine()
    asyncio.get_event_loop().run_until_complete(engine.start_analysis(float(runtime)))
     # graph plotting
    # countrywise action graph
    plt.figure("Per country action")
    plt.bar([k for k in engine.country_wise_action],[engine.country_wise_action[k] for k in engine.country_wise_action])
            
    # trending users > 1 posts
    plt.figure("user contributions > 1 updates")
    plt.bar([k for k in engine.contributing_users if engine.contributing_users[k] > 1 ],[engine.contributing_users[k] for k in engine.contributing_users if  engine.contributing_users[k] > 1])

    # insertion , deletion and edits
    plt.figure("edits/insersts/creations/deletions")
    plt.bar(["edits","inserts","creations","deletions"],[engine.edits,engine.inserts,engine.create,engine.deletes])

    plt.figure("patrolled/unpatrolled edits")
    plt.pie([engine.patrolled_edits, engine.unpatrolled_edits],labels=["patrolled edits", "un patrolled edits"])   

    print("bot updation: {}".format(engine.bot_actions))
    plt.show()