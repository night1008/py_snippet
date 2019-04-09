import base64
import json

def data2bs64(data):
    data_str = json.dumps(data)
    bs64_str = base64.b64encode(bytes(data_str, 'utf-8')).decode('utf-8')
    return bs64_str.replace('+', '-').replace('/', '_').rstrip('=')

if __name__ == '__main__':
    print('enter __main__')
    teams = {
        'action': 'join_team',
        'groupServerId': 1,
        'members': [
            [5283843, "狂暴者特伦斯", 0, 1, 4, 0, "青铜III", 1217],
            [5677057, "神采的黑龙", 1, 1, 1, 1, "青铜V", 1097]
        ],
        'pid': 5677057,
        'platKey': 'taptap',
        'share_ver': 1,
        'team_mode': 4,
        'top_one_times': 0,
        'war_times': 0
    }
    print(data2bs64(teams))