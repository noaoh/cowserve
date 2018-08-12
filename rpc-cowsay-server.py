#!/usr/bin/env python
from flask import Flask
from flask_restful import Api, reqparse, Resource
from pysay.scripts.pysay import cowsay as _cowsay, Appearance

app = Flask(__name__)
api = Api(app)


cowparser = reqparse.RequestParser()
cowparser.add_argument("f", help="The cow to say the message with.", default="default")
cowparser.add_argument("m", help="The message for the cow to say.", required=True)
cowparser.add_argument("b", help="eyes are '==' (borg)", dest="borg", default=True, store_missing=False)
cowparser.add_argument("d", help="eyes are 'xx' and tongue is 'U ' (dead)", dest="dead", default=True, store_missing=False)
cowparser.add_argument("g", help="eyes are '$$' (greedy)", default=True, dest="greedy", store_missing=False)
cowparser.add_argument("p", help="eyes are '@@' (paranoid)", default=True, dest="paranoid", store_missing=False)
cowparser.add_argument("s", help="eyes are '**' and tongue is 'U ' (stoned)", dest="stoned", default=True, store_missing=False)
cowparser.add_argument("t", help="eyes are '--' (tired)", default=True, dest="tired", store_missing=False)
cowparser.add_argument("w", help="eyes are 'OO' (wired)", default=True, dest="w", store_missing=False)
cowparser.add_argument("y", help="eyes are '..' (young)", default=True, dest="young")
cowparser.add_argument("n", help=("disable word wrap and ignore -W,"
                                  " allowing FIGlet and ASCII art"), dest="expand", default=True, store_missing=False)
cowparser.add_argument("W", type=int, help=("maximum width for the text within the"
                                            " balloon (default: 40)"), dest="columns", default=40)
cowparser.add_argument("e", help="must be a quoted string of two characters", dest="eyes", default="oo")
cowparser.add_argument("T", help="must be a quoted string of two characters", dest="tongue", default="  ")


class Cowsay(Resource):
    def post(self):
        args = cowparser.parse_args()
        message = args.pop("m")
        cow = args.pop("f")
        return {"message": _cowsay(cow=cow, message=message, a=Appearance(**args))}


class Cowthink(Resource):
    def post(self):
        args = cowparser.parse_args()
        message = args.pop("m")
        cow = args.pop("f")
        return {"message": _cowsay(cow=cow, message=message, a=Appearance(**args, thinking=True))}


api.add_resource(Cowsay, "/api/cowsay")
api.add_resource(Cowthink, "/api/cowthink")


"""
def main():
    app.run(debug=True, host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
"""
