CREATE TABLE Profiles (
    profile_id SERIAL PRIMARY KEY,
    bio TEXT,
    fecha_nacimiento DATE NOT NULL, -- Usado para calcular rango de edad
    gender VARCHAR(50),
    location_address VARCHAR(255),
    city VARCHAR(100),
    sports_interests TEXT,
    search_radius INTEGER, -- En kilómetros
    languages TEXT
);