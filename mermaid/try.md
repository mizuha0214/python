```mermaid
graph TD
    %% 時間表示（四角なし）
    subgraph 時間
        T1(["T1"]):::time ~~~ T2(["T2"]):::time ~~~ T3(["T3"]):::time ~~~ T4(["T1"]):::time ~~~
        T5(["T1"]):::time ~~~ T6(["T1"]):::time
        style T1 fill-opacity:0, stroke-opacity:0;
        style T2 fill-opacity:0, stroke-opacity:0;
        style T3 fill-opacity:0, stroke-opacity:0;
    end

    %% 並行処理
    subgraph フロー1
        A1[処理A1] ~~~ A2[処理A2] --> A3[処理A3]
    end

    subgraph フロー2
        B1[処理B1] --> B2[処理B2] --> B3[処理B3]
    end

    subgraph フロー3
        C0[処理C0] --> C1[処理C1] --> C2[処理C2] --> C3[処理C3]
    end

    %% 収束処理
    結果処理(["処理終了<br>（3フロー分の横幅）"])

    %% 矢印接続
    A3 --> 結果処理
    B3 --> 結果処理
    C3 --> 最終処理(["最終処理"])
    結果処理 --> 最終処理
