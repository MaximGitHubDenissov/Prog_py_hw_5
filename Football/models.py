import csv
import user_input as ui
def create_game():
    headers = ['Date','Frst_tm','Frst_tm_res','Sec_tm','Sec_tm_res']
    with open('game.csv', 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=headers, delimiter=';', lineterminator='\n')
        csv_writer.writeheader()

def create_tournt_tb():
    headers = ['Team_name', 'Total_games', 'Victory', 'Draw', 'Defeat', 'Total_score']
    with open ('tornt_tb.csv', 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=headers, delimiter=';', lineterminator='\n')
        csv_writer.writeheader()

def add_game():
    headers = ['Date','Frst_tm','Frst_tm_res','Sec_tm','Sec_tm_res']
    with open('game.csv', 'a') as f:
        date = ui.date_input()
        frst_tm = ui.team_input('первой') 
        frst_tm_res = ui.score_input(frst_tm)
        scnd_tm = ui.team_input('второй')
        scnd_tm_res = ui.score_input(scnd_tm)
        csv_writer = csv.DictWriter(f, fieldnames=headers, delimiter=';', lineterminator='\n')
        csv_writer.writerow({'Date': date, 'Frst_tm':frst_tm, 'Frst_tm_res':frst_tm_res,\
            'Sec_tm': scnd_tm, 'Sec_tm_res': scnd_tm_res})
    return frst_tm, frst_tm_res, scnd_tm, scnd_tm_res

def tourn_tb_change(ft, fs, st, ss):
    res = []
    with open('tornt_tb.csv', 'r') as f:
        csv_reader = csv.DictReader (f, delimiter=';')
        for row in csv_reader:
            res.append(dict(row)) 

    for i in range(len(res)):
        if res[i]['Team_name'] == ft:
            first = res[i]
            frst_idx = i
        if res[i]['Team_name'] == st:
            second = res[i]
            scnd_idx = i
    if fs > ss:
        first['Victory'] = str(int(first['Victory']) + 1)
        first['Total_score'] = str(int(first['Total_score'])+3)
        second['Defeat'] = str(int(second['Defeat'])+1)
    elif fs == ss:
        first['Draw'] = str(int(first['Draw']) +1)
        second['Draw'] = str(int(second['Draw'])+1)
        first['Total_score'] = str(int(first['Total_score'])+1)
        second['Total_score'] = str(int(second['Total_score'])+1)
    else:
        second['Victory'] = str(int(second['Victory']) + 1)
        second['Total_score'] = str(int(second['Total_score'])+3)
        first['Defeat'] = str(int(first['Defeat'])+1)

    first['Total_games'] = str(int(first['Total_games'])+1)
    second['Total_games'] = str(int(second['Total_games'])+1)
    
    res[frst_idx] = first
    res[scnd_idx] = second

    headers = ['Team_name', 'Total_games', 'Victory', 'Draw', 'Defeat', 'Total_score']
    with open ('tornt_tb.csv', 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=headers, delimiter=';', lineterminator='\n')
        csv_writer.writeheader()
        csv_writer.writerows(res)





