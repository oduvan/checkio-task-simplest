from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee




api.add_listener(ON_CONNECT, CheckiOReferee([
        ["Basics",[
                ['2+3=?', [2,3], 5, 'EXT1'],
                ['2+7=?', [2,7], 9]
            ]
        ],
        ["Addition",[
                ['6+3=?', [6,3], 9],
                ['6+7=?', [6,7], 13, 'EXT2']
            ]
        ]
    ])
