from flask import Flask
from flask import send_file
from flask_restful import reqparse, abort, Api, Resource
from generator import generate_new_tombstone

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, location=["json"], required=True)
parser.add_argument('inscription', type=str, location=["json"], required=True)


class GenerateTombstone(Resource):

    def post(self):
        args = parser.parse_args()
        out_file_name = generate_new_tombstone(args.name, args.inscription)
        return send_file("created_tombstones/{}.png".format(out_file_name), mimetype='image/png')


api.add_resource(GenerateTombstone, '/generate_tombstone')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
