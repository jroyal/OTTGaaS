from flask import Flask, request, jsonify
from flask import send_file
from flask_restful import reqparse, abort, Api, Resource
from generator import generate_new_tombstone
import os
import re

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('inscription', type=str, required=True)


class GenerateTombstone(Resource):

    def post(self):
        """
        Generate and return the png tombstone file
        """
        args = parser.parse_args()
        out_file_name = generate_new_tombstone(args.name, args.inscription)
        return send_file("created_tombstones/{}.png".format(out_file_name), mimetype='image/png')

class Tombstone(Resource):

    def get(self, tomb_name):
        """
        Return a previously generated tombstone
        """
        file_name = "created_tombstones/{}.png".format(tomb_name)
        if os.path.isfile(file_name):
            return send_file(file_name, mimetype='image/png')
        else:
            return "Unable to find tombstone {}".format(tomb_name), 404

class SlackTombstone(Resource):

    def post(self):
        """
        Accepts a request from a slack slash command to create and return a tombstone
        """
        print request.form
        question_match = re.search("name (.+) inscription (.+)", request.form["text"])

        if question_match:
            name = question_match.group(1)
            inscription = question_match.group(2)
            out_file_name = generate_new_tombstone(name, inscription)
        else:
            return "Malformed Request. Your text needs `name` and `inscription` in it."

        data = {
            "text": "Here's your tombstone",
            "response_type": "in_channel",
            "attachments": [
                {
                    "fallback": "Something broke",
                    "image_url": "https://ottgaas.mybluemix.net/tombstone/{}".format(out_file_name)
                }
            ]
        }
        return jsonify(**data)

api.add_resource(GenerateTombstone, '/generate_tombstone')
api.add_resource(SlackTombstone, '/slack_generate_tombstone')
api.add_resource(Tombstone, '/tombstone/<string:tomb_name>')

if __name__ == '__main__':
    # Support Bluemix CF app port
    port = int(os.getenv('VCAP_APP_PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
