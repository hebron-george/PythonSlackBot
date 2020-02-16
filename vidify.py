import os
from flask import abort, Flask, jsonify, request
import os.path
app = Flask(__name__)


def is_request_valid(request):
	if (os.environ['FLASK_ENV'] == 'development'):
		return True

	is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
	is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']
	return is_token_valid and is_team_id_valid


@app.route('/hello-there', methods=['POST'])
def hello_there():
	if not is_request_valid(request):
		abort(400)

	user_name = ""
	if ('user_name' in request.args):
		user_name = str(request.args['user_name'])

	return jsonify(
		response_type='in_channel',
		text='<https://www.youtube.com/watch?v=42Og4uROeHg&t=11s|General |||' + user_name + '||| Kenobi!>',
	)
