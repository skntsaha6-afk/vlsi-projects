                start_bot.py
                     │
                     ▼
                 Authentication
                     │
                     ▼
                Broker Client
                     │
                     ▼
                 WebSocket Data
                     │
                     ▼
                 Trading Agent
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
     Strategy     Risk Mgmt   Execution
         │           │           │
         └───────────▼───────────┘
                     │
                     ▼
                  FYERS API

##### Correct Architecture Now ###### 
trading_agent
│
├── agents
│   └── trading_agent.py
│
├── auth
│   ├── flask_auth_server.py
│   ├── generate_auth_code.py
│   ├── token_reader.py
│   └── access_token.txt
│
├── execution
│   ├── fyers_client.py
│   └── order_manager.py
│
├── strategies
├── data
├── websocket
├── utils
├── risk_management
│
├── bot.py
└── requirements.txt