from flask import Flask, render_template, url_for, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from backend import Backend
app = Flask(__name__)
api = Api(app)
CORS(app, origins="http://127.0.0.1:5000", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)

backend = Backend()

def abort_if_season_doesnt_exist(season):
    if not backend.does_season_exist(season):
        abort(404, message="This season doesn't exist in our database")

def abort_if_team_doesnt_exist(season, team):
    if not backend.does_team_exist(season, team):
        abort(404, message="This team doesn't exist in this season in our database")


@app.route('/api/equivalent/<origin_se>/<team>/<new_se>')
def get_team_equivalent(origin_se, team, new_se):
    abort_if_season_doesnt_exist(origin_se)
    abort_if_season_doesnt_exist(new_se)
    abort_if_team_doesnt_exist(origin_se, team)
    result = backend.get_alike_team(team, old=origin_se, new=new_se)
    return jsonify(result)

@app.route('/api/<season>/teams')
def teams(season):
    abort_if_season_doesnt_exist(season)
    teams = backend.get_teams_by_season(season)
    return jsonify(teams)


@app.route('/api/seasons')
def seasons():
    seasons = backend.get_season()
    return jsonify(seasons)

@app.route('/')
def home():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)