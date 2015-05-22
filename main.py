
# these tests are pretty bad, mostly to make sure no exceptions are thrown

import time
from riotwatcher import RiotWatcher, NORTH_AMERICA

key = '4f7e4341-80cb-4e38-8157-697f000e64ad'
# if summoner doesnt have ranked teams, teams tests will fail
# if summoner doesnt have ranked stats, stats tests will fail
# these are not graceful failures, so try to use a summoner that has them
summoner_name = 'Canadian Carry'

w = RiotWatcher(key)


def wait():
    while not w.can_make_request():
        time.sleep(1)


def champion_tests():
    wait()
    temp = w.get_all_champions()
    wait()
    w.get_champion(temp['champions'][0]['id'])


def current_game_tests():
    wait()
    player = w.get_featured_games()['gameList'][0]['participants'][0]['summonerName']
    wait()
    player_id = w.get_summoner(name=player)['id']
    wait()
    w.get_current_game(player_id)


def featured_games_tests():
    wait()
    w.get_featured_games()


def game_tests(summoner):
    wait()
    w.get_recent_games(summoner['id'])


def league_tests(summoner):
    wait()
    w.get_league(summoner_ids=[summoner['id'], ])
    wait()
    w.get_league_entry(summoner_ids=[summoner['id'], ])
    wait()
    w.get_challenger()


def static_tests():
    temp = w.static_get_champion_list()
    w.static_get_champion(temp['data'][list(temp['data'])[0]]['id'])
    temp = w.static_get_item_list()
    w.static_get_item(temp['data'][list(temp['data'])[0]]['id'])
    temp = w.static_get_mastery_list()
    w.static_get_mastery(temp['data'][list(temp['data'])[0]]['id'])
    w.static_get_realm()
    temp = w.static_get_rune_list()
    w.static_get_rune(temp['data'][list(temp['data'])[0]]['id'])
    temp = w.static_get_summoner_spell_list()
    w.static_get_summoner_spell(temp['data'][list(temp['data'])[0]]['id'])
    w.static_get_versions()


def status_tests():
    w.get_server_status()
    w.get_server_status(region=NORTH_AMERICA)


def match_tests(match):
    wait()
    w.get_match(match['matchId'])


def match_history_tests(summoner):
    wait()
    ms = w.get_match_history(summoner['id'])
    return ms['matches'][0]


def stats_tests(summoner):
    wait()
    w.get_stat_summary(summoner['id'])
    wait()
    w.get_ranked_stats(summoner['id'])


def summoner_tests(summoner_name):
    wait()
    s = w.get_summoner(name=summoner_name)
    wait()
    w.get_summoner(_id=s['id'])
    wait()
    w.get_mastery_pages([s['id'], ])
    wait()
    w.get_rune_pages([s['id'], ])
    wait()
    w.get_summoner_name([s['id'], ])
    return s


def team_tests(summoner):
    wait()
    t = w.get_teams_for_summoner(summoner['id'])
    wait()
    w.get_team(t[0]['fullId'])


def main():

    crapsticks = 1
    while crapsticks == 1: 
    
        command = input("Enter a command: ")
    
        if "version" in command:
            print("The newest Leauge of Legends version is "+ w.static_get_versions()[0])
    
        if "champ title" in command:
            champion = input("Enter a champion name: ")
            static_champ_list = w.static_get_champion_list()
            print(static_champ_list['data'][champion]['title'])

        if "stats" in command:
            username = input("Enter a summoner name: ")
            me = w.get_summoner(name=username)
            stats = w.get_stat_summary(me['id'])
    
            print("Your username is " + me['name'] + ".")
            print("You are level " + str(me['summonerLevel']) + ".")
            i=0
            while i<len(stats['playerStatSummaries']):
                print("In " + stats['playerStatSummaries'][i]['playerStatSummaryType'] + " you have " + str(stats['playerStatSummaries'][i]['wins']) + " wins.")
                i+=1
        
        
        if "masteries" in command:
            username = input("Enter a summoner name: ")
            me = w.get_summoner(name=username)
            player_id = w.get_summoner(username)['id']
            my_mastery_pages =  w.get_mastery_pages([me['id'], ])
            print(username + " has " + str(len(my_mastery_pages[str(player_id)]['pages'])) + " mastery pages.")
            i=0
            while i<len(my_mastery_pages[str(player_id)]['pages']):
                print(my_mastery_pages[str(player_id)]['pages'][i]['name'])
                i+=1
            
        
        
    

if __name__ == '__main__':
    main()
