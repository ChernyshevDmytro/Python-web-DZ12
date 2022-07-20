DROP TABLE IF EXISTS prices;
CREATE TABLE prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brain_price INT(6),  
    telemart_price INT(6), 
    compx_price INT(6),    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


