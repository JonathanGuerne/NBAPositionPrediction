import pandas as pd

import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler



def remove_slash_name(_df):
    df = _df.copy()
    df['Player'] = df['Player'].apply(lambda row: row.split('\\')[0])
    df['Player'] = df['Player'].apply(lambda row: row.split('*')[0])
    return df


def remove_rk(_df):
    df = _df.copy()
    return df.drop(['Rk'], axis=1)


def remove_team(_df):
    df = _df.copy()
    return df.drop(['Tm'], axis=1)


def remove_age(_df):
    df = _df.copy()
    return df.drop(['Age'], axis=1)


def remove_game(_df):
    df = _df.copy()
    return df.drop(['G'], axis=1)


def remove_game_started(_df):
    df = _df.copy()
    return df.drop(['GS'], axis=1)


def remove_min(_df):
    df = _df.copy()
    return df.drop(['MP'], axis=1)


def extract_name_position(_df):
    df = _df.copy()
    return _df.drop(['Pos', 'Player'], axis=1), _df[['Player', 'Pos']]


def remove_nan(_df):
    df = _df.copy()
    return df.dropna(axis=1, how='all').fillna(0)


class Backend():

    dfs = {}
    seasons = []


    def get_alike_team(self, team, old='95-96', new='18-19'):
        # we use pandas to load data directly from csv
        df = pd.read_csv('../data/adv_stats_{}.csv'.format(old))

        print(len(df))

        # apply a couple of preprocessing function
        df = remove_rk(remove_slash_name(df))
        df = df.loc[df['Tm'] == team]
        df = remove_age(remove_team(df))
        df = remove_game(remove_min(df))

        pos_used = ['PG','SG','SF','PF','C']
        df = df.loc[df['Pos'].isin(pos_used)]
        df = remove_nan(df)

        df_old_team, df_old_names = extract_name_position(df)

        df = pd.read_csv('../data/adv_stats_{}.csv'.format(new))

        df = remove_rk(remove_slash_name(df))
        df = remove_age(remove_team(df))
        df = remove_game(remove_min(df))

        pos_used = ['PG','SG','SF','PF','C']
        df = df.loc[df['Pos'].isin(pos_used)]
        df = remove_nan(df)

        df_current_player, df_current_names = extract_name_position(df)
        neigh = NearestNeighbors(1, metric='sqeuclidean')

        scaler = MinMaxScaler()

        neigh.fit(scaler.fit_transform(df_current_player.values))

        dst, ids = neigh.kneighbors(scaler.transform(df_old_team.values))
        result_df = pd.DataFrame({'original' : (df_old_names.values)[:,0],
        'new' : df_current_names.iloc[np.reshape(ids,-1)].values[:,0]})
        
        return result_df.to_dict()

    def __init__(self):
        
        import glob
        self.seasons = ([f.split("_")[-1].split('.')[0] for f in glob.glob("../data/*.csv")])
    
    def does_season_exist(self, season):
        return season in self.seasons

    def does_team_exist(self, season, team):
        return team in self.get_teams_by_season(season)

    def get_teams_by_season(self, season):  
        df = pd.read_csv('../data/adv_stats_{}.csv'.format(season))
        a = np.unique(df['Tm'])
        a = a.tolist()
        if 'TOT' in a :
            a.remove('TOT')
        return a

    def get_season(self):
        if self.seasons is not None:
            return self.seasons
        else:
            return None