erDiagram
    USER ||--o{ ASSESSMENT : "takes"
    
    USER {
        int id PK
        string username
        string password
        string email
    }
    
    ASSESSMENT {
        int id PK
        int user_id FK "Nullable"
        datetime taken_at
        int q1_to_q9 "Values 0-3"
        int q10_difficulty
        int total_score
        string severity
    }
