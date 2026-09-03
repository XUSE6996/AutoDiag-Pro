CREATE TABLE IF NOT EXISTS dtc (

    id INTEGER PRIMARY KEY,

    code TEXT UNIQUE,

    description TEXT

);


INSERT INTO dtc(code, description)
VALUES
(
    'P0300',
    'Zündaussetzer erkannt – mehrere Zylinder'
),

(
    'P0420',
    'Katalysator Wirkungsgrad unter Grenzwert'
),

(
    'P0171',
    'Gemisch zu mager Bank 1'
),

(
    'P0301',
    'Zündaussetzer Zylinder 1'
),

(
    'U0100',
    'Kommunikationsfehler Motorsteuergerät'
);
