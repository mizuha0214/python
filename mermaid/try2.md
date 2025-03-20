```mermaid
graph TD
subgraph フロー2 
        B1[処理B1] --> B2[処理B2] --> B3[処理B3]
    end

    subgraph フロー3
        C0[処理C0] ~~~ Dummy[" "]:::invisible ~~~ C1[処理C1] 
    end
    classDef invisible fill-opacity:0,stroke-opacity:0;

    