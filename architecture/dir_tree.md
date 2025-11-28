## Directory Tree

```
C:.
│   .env
│   .gitignore
│   logging.ini
│   pyproject.toml
│   README.md
│
├───architecture
│       dir_tree.md
│       module_view.md
│
├───logs
│       wealthboard-hexagonal.log
│
├───resources
├───src
│   ├───wealthboard
│   │   │   main.py
│   │   │   __init__.py
│   │   │
│   │   ├───common
│   │   │   ├───adapters
│   │   │   │   ├───driven
│   │   │   │   │   │   yfinance_price_provider.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           yfinance_price_provider.cpython-312.pyc
│   │   │   │   │
│   │   │   │   └───driving
│   │   │   ├───app
│   │   │   │   └───ports
│   │   │   │       │   price_provider.py
│   │   │   │       │
│   │   │   │       └───__pycache__
│   │   │   │               price_provider.cpython-312.pyc
│   │   │   │
│   │   │   └───infrastructure
│   │   │       ├───db
│   │   │       │   │   oracle_connection_provider.py
│   │   │       │   │   __init__.py
│   │   │       │   │
│   │   │       │   └───__pycache__
│   │   │       │           connection_provider.cpython-312.pyc
│   │   │       │           oracle_connection_provider.cpython-312.pyc
│   │   │       │           __init__.cpython-312.pyc
│   │   │       │
│   │   │       └───logging
│   │   │           │   log_config.py
│   │   │           │
│   │   │           └───__pycache__
│   │   │                   log_config.cpython-312.pyc
│   │   │
│   │   ├───crypto
│   │   │   ├───adapters
│   │   │   │   ├───driven
│   │   │   │   └───driving
│   │   │   ├───app
│   │   │   └───domain
│   │   ├───etf
│   │   │   ├───adapters
│   │   │   │   ├───decorators
│   │   │   │   │   │   cache_owned_etf_repository.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           cached_owned_etf_repository.cpython-312.pyc
│   │   │   │   │           cache_owned_etf_repository.cpython-312.pyc
│   │   │   │   │
│   │   │   │   ├───driven
│   │   │   │   │   │   oracle_etf_history_repository.py
│   │   │   │   │   │   oracle_etf_repository.py
│   │   │   │   │   │   oracle_owned_etf_repository.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           oracle_etf_history_repository.cpython-312.pyc
│   │   │   │   │           oracle_etf_repository.cpython-312.pyc
│   │   │   │   │           oracle_owned_etf_repository.cpython-312.pyc
│   │   │   │   │
│   │   │   │   └───driving
│   │   │   ├───app
│   │   │   │   ├───dto
│   │   │   │   │   │   owned_etf_dto.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           owned_etf_dto.cpython-312.pyc
│   │   │   │   │
│   │   │   │   ├───mapper
│   │   │   │   │   │   owned_etf_mapper.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           owned_etf_mapper.cpython-312.pyc
│   │   │   │   │
│   │   │   │   ├───ports
│   │   │   │   │   │   etf_history_repository.py
│   │   │   │   │   │   etf_repository.py
│   │   │   │   │   │   owned_etf_repository.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           etf_history_repository.cpython-312.pyc
│   │   │   │   │           etf_repository.cpython-312.pyc
│   │   │   │   │           owned_etf_repository.cpython-312.pyc
│   │   │   │   │
│   │   │   │   ├───service
│   │   │   │   │   │   etf_history_service.py
│   │   │   │   │   │   etf_service.py
│   │   │   │   │   │   owned_etf_service.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           etf_history_service.cpython-312.pyc
│   │   │   │   │           etf_service.cpython-312.pyc
│   │   │   │   │           owned_etf_service.cpython-312.pyc
│   │   │   │   │
│   │   │   │   └───use_cases
│   │   │   │       │   add_owned_etf.py
│   │   │   │       │   calculate_metrics.py
│   │   │   │       │   multiple_metrics.py
│   │   │   │       │   portfolio_projection.py
│   │   │   │       │
│   │   │   │       └───__pycache__
│   │   │   │               add_owned_etf.cpython-312.pyc
│   │   │   │               calculate_metrics.cpython-312.pyc
│   │   │   │               multiple_metrics.cpython-312.pyc
│   │   │   │               portfolio_metrics.cpython-312.pyc
│   │   │   │
│   │   │   └───domain
│   │   │       │   etf.py
│   │   │       │   etf_history.py
│   │   │       │   owned_etf.py
│   │   │       │   __init__.py
│   │   │       │
│   │   │       └───__pycache__
│   │   │               etf.cpython-312.pyc
│   │   │               etf_history.cpython-312.pyc
│   │   │               owned_etf.cpython-312.pyc
│   │   │               __init__.cpython-312.pyc
│   │   │
│   │   └───__pycache__
│   │           __init__.cpython-312.pyc
│   │
│   └───wealthboard_hexagonal.egg-info
│           dependency_links.txt
│           PKG-INFO
│           requires.txt
│           SOURCES.txt
│           top_level.txt
│
└───test
```