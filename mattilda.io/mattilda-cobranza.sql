-- Tabla para almacenar la información de las escuelas
CREATE TABLE Escuelas (
    id_escuela INTEGER PRIMARY KEY,
    nombre_escuela TEXT NOT NULL,
    direccion TEXT
    -- Otros campos relacionados con la escuela
);

-- Tabla para almacenar la información de los administradores por escuela
CREATE TABLE Administradores (
    id_administrador INTEGER PRIMARY KEY,
    id_escuela INTEGER,
    nombre_administrador TEXT NOT NULL,
    puesto TEXT,
    -- Otros campos relacionados con el administrador
    FOREIGN KEY (id_escuela) REFERENCES Escuelas (id_escuela)
);

-- Tabla para almacenar la información de los padres
CREATE TABLE Padres (
    id_padre INTEGER PRIMARY KEY,
    nombre_padre TEXT NOT NULL,
    direccion TEXT
    -- Otros campos relacionados con el padre
);

-- Tabla para almacenar la información de los hijos
CREATE TABLE Hijos (
    id_hijo INTEGER PRIMARY KEY,
    id_padre INTEGER,
    nombre_hijo TEXT NOT NULL,
    fecha_nacimiento DATE,
    -- Otros campos relacionados con el hijo
    FOREIGN KEY (id_padre) REFERENCES Padres (id_padre)
);

-- Tabla para almacenar la información de los pagos
CREATE TABLE Pagos (
    id_pago INTEGER PRIMARY KEY,
    id_escuela INTEGER,
    id_padre INTEGER,
    id_hijo INTEGER,
    monto DECIMAL(10,2) NOT NULL,
    fecha_pago DATE NOT NULL,
    -- Otros campos relacionados con el pago
    FOREIGN KEY (id_escuela) REFERENCES Escuelas (id_escuela),
    FOREIGN KEY (id_padre) REFERENCES Padres (id_padre),
    FOREIGN KEY (id_hijo) REFERENCES Hijos (id_hijo)
);

