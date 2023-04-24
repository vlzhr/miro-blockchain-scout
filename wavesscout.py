from requests import get, post
from json import loads, dumps
from re import findall
from math import fabs


access_token = "SEE README.md"


def create_board(name="My New Board"):
    board_params = {
      "description": "Waves Blockchain account's connections board. Created by @vlzhr.",
      "name": name,
      "policy": {
        "permissionsPolicy": {
          "collaborationToolsStartAccess": "all_editors",
          "copyAccess": "anyone",
          "sharingAccess": "team_members_with_editing_rights"
        },
        "sharingPolicy": {
          "access": "private",
          "inviteToAccountAndBoardLinkAccess": "no_access",
          "organizationAccess": "private",
          "teamAccess": "private"
        }
      }
    }
    return loads(post("https://api.miro.com/v2/boards", json=board_params, headers={"Authorization": "Bearer "+access_token}).text).get("id", "none")


def create_card(text, x=0, y=0):
    params = {
        "data": {
            "title": text
        },
        "position": {
            "origin": "center",
            "x": x,
            "y": y
        }
    }
    return loads(post("https://api.miro.com/v2/boards/"+board_id+"/cards", json=params, headers={"Authorization": "Bearer "+access_token}).text).get("id", "none")


def create_connection(fr, to, text=""):
    params = {
        "startItem": {
            "id": fr
        },
        "endItem": {
            "id": to
        },
        "captions": [
            {"content": text}
        ]
    }
    return loads(post("https://api.miro.com/v2/boards/"+board_id+"/connectors", json=params, headers={"Authorization": "Bearer "+access_token}).text).get("id", "none")


def draw_connections(connections, main_block):
    i = connections["in"]
    i_keys = list(i.keys())
    width = len(i_keys) * 100
    for c in range(len(i_keys)):
        toid = create_card(i_keys[c], int(-0.75*width) + int(fabs(-width / 2 + width * c / len(i_keys))), -int(width / 2 - width * c / len(i_keys)))
        print("in connection added", create_connection(toid, main_block, i[i_keys[c]]))

    o = connections["out"]
    o_keys = list(o.keys())
    width = len(o_keys) * 100
    for c in range(len(o_keys)):
        toid = create_card(o_keys[c], -(int(-0.75*width) + int(fabs(-width / 2 + width * c / len(o_keys)))), -int(width / 2 - width * c / len(o_keys)))
        print("out connection added", create_connection(main_block, toid, o[o_keys[c]]))



def get_account_connections(address):
    data = get("https://w8.io/{}/t/4".format(address)).text
    lines = data.split("\n")
    lines = [findall(">([a-z0-9A-Z:\.\+\- ]+)<", n) for n in lines if "transfer" in n and n.startswith("<small>") or n.startswith("<b><small>") or n.startswith('</pre></td><td valign="top"><pre><small>')]
    in_connections = {n[-1]: n[0] for n in lines if "+" in n[3] and n[-4] != address}
    out_connections = {n[-4]: n[0] for n in lines if "+" not in n[3] and n[-4] != " " and n[-4] != address and len(n[-4]) == 35}
    return {"in": in_connections, "out": out_connections}


def main(address):
    global board_id
    board_id = create_board("Connections "+address)
    main_card = create_card(address)
    print("Miro board created")
    data = get_account_connections(address)
    print("address: ", address)
    print("connections: ", len(data["in"]), "in", len(data["out"]), "out")
    print()
    draw_connections(data, main_card)
    print("finished")

