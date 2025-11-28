Module Dependency View


``` mermaid
    flowchart BT


        subgraph Domain
            D{{etf, etf_history, owned_etf}}
        end
        
        subgraph Ports
            P{{etf_repository, etf_history_repository, owned_etf_repository}}
        end

        subgraph Services
            S{{etf_service, etf_history_service, owned_etf_service}}
        end
        
        subgraph DrivenAdapters
            DRIVENA{{oracle_etf_repository, oracle_etf_history_repository, oracle_owned_etf_repository}}
        end

        subgraph UseCase
            UC{{calculate_metrics, mutiple_metrics}}
        end

    style Domain fill: 

    DRIVENA --> P
    DRIVENA --> D
    P --> D
    S --> P
    S --> D
    UC --> S

        %% Styles
    style Domain fill:#2a9d8f,stroke:#264653,color:white
    style Ports fill:#457b9d,stroke:#1d3557,color:white
    style Services fill:#b5838d,stroke:#6d6875,color:white
    style DrivenAdapters fill:#e76f51,stroke:#d62828,color:white
    style UseCase fill:#8ac926,stroke:#6a994e,color:white

```