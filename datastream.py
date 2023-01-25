import asyncio
import data_engine.data_engine as analyser
import matplotlib.pyplot as plt

def plot_graph(analyser: analyser.DataEngine) -> None:
    """
        function to plot graphs with the data from data engine
    """
     # graph plotting
    # countrywise action graph
    plt.figure("Per country action")
    plt.bar([k for k in analyser.country_wise_action],[analyser.country_wise_action[k] for k in analyser.country_wise_action])
            
    # trending users > 1 posts
    plt.figure("user contributions > 1 updates")
    plt.bar([k for k in analyser.contributing_users if analyser.contributing_users[k] > 1 ],[analyser.contributing_users[k] for k in analyser.contributing_users if  analyser.contributing_users[k] > 1])

    # insertion , deletion and edits
    plt.figure("edits/insersts/creations/deletions")
    plt.bar(["edits","inserts","creations","deletions"],[analyser.edits,analyser.inserts,analyser.create,analyser.deletes])

    plt.figure("patrolled/unpatrolled edits")
    plt.pie([analyser.patrolled_edits, analyser.unpatrolled_edits],labels=["patrolled edits", "un patrolled edits"])   

    print("bot updation: {}".format(analyser.bot_actions))
    print("total actions happening on wiki :{}".format(analyser.total_actions))
    plt.show()

if __name__ == "__main__": 
    runtime = name = input("How long you want to run this script for(please enter in seconds): ") 
    engine = analyser.DataEngine()
    asyncio.get_event_loop().run_until_complete(engine.start_analysis(float(runtime)))
    plot_graph(engine)
    