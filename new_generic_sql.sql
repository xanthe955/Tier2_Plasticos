CREATE TABLE solicitudes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    carcasa_color_azul INT,
    carcasa_color_verde INT,
    carcasa_color_amarillo INT,
    carcasa_color_morado INT,
    carcasa_color_rosa INT,
    carcasa_color_cyan INT
);
CREATE TABLE partners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    details VARCHAR(255),
    direction VARCHAR(255),
    api_endpoint VARCHAR(255),
    props JSON,
    enabled BOOLEAN
);

INSERT INTO partners (name, details, direction, api_endpoint, props, enabled)
VALUES
    ('T2A PE', 'Tier 2 Proveedor de Piezas Electronicas', 'Direction 1 T2A', 'http://api.example.com/partner1', '{"key": "value1"}', 1),
    ('T2B PC', 'Tier 2 Proveedor de Piezas Cosmeticas', 'Direction T2B', 'http://api.example.com/partner2', '{"key": "value3"}', 1);

CREATE TABLE raw_materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    props JSON,
    stock INT,
    enabled BOOLEAN
);

INSERT INTO raw_materials (name, description, props, stock, enabled)
VALUES
    ('Cameras', 'Cameras for iPhone', '{"key": "value1"}', 100, 1),
    ('Biometric Sensor', 'Biometric Sensor for iPhone 3rd Gen', '{"key": "value2"}', 200, 1),
    ('Baseband', 'Baseband for iPhone 1aa', '{"key": "value3"}', 150, 1),
    ('Power Management', 'Power Management for iPhone', '{"key": "value3"}', 100, 1),
    ('Processor', 'Processor Apple A14 Bionic', '{"key": "value3"}', 150, 1),
    ('NAND', 'NAND 128 gb 3rd gen', '{"key": "value3"}', 200, 1),
    ('DRAM', 'DRAM 1 gb ', '{"key": "value3"}', 150, 1),
    ('Acelerometer', 'Gyroscope 6-axis for iPhone', '{"key": "value3"}', 100, 1),
    ('Battery', 'Battery 1000 mAh', '{"key": "value3"}', 150, 1),
    ('Microphone', 'Microphone for iPhone', '{"key": "value3"}', 150, 1),
    ('Speakers', 'Speakers mono iPhone', '{"key": "value3"}', 150, 1),
    ('Carcasa Azul', 'Carcasa color Azul', '{"key": "value3"}', 150, 1),
    ('Carcasa Verde', 'Carcasa color Verde', '{"key": "value3"}', 150, 1),
    ('Carcasa Amarillo', 'Carcasa color Amarillo', '{"key": "value3"}', 150, 1),
    ('Carcasa Morado', 'Carcasa color Morado', '{"key": "value3"}', 150, 1),
    ('Carcasa Rosa', 'Carcasa color Rosa', '{"key": "value3"}', 150, 1),
    ('Carcasa Cyan', 'Carcasa color Cyan', '{"key": "value3"}', 150, 1);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    props JSON,
    stock INT,
    enabled BOOLEAN
);


INSERT INTO products (name, description, props, stock, enabled)
VALUES
    ('iPhone Azul', 'Smartphone iPhone color Azul', '{"key": "value1"}', 50, 1),
    ('iPhone Verde', 'Smartphone iPhone color Verde', '{"key": "value1"}', 55, 1),
    ('iPhone Amarillo', 'Smartphone iPhone color Amarillo', '{"key": "value1"}', 60, 1),
    ('iPhone Morado', 'Smartphone iPhone color Morado', '{"key": "value1"}', 65, 1),
    ('iPhone Rosa', 'Smartphone iPhone color Rosa', '{"key": "value1"}', 50, 1),
    ('iPhone Cyan', 'Smartphone iPhone color Cyan', '{"key": "value1"}', 55, 1);


CREATE TABLE raw_materials_partners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    raw_material_id INT,
    partner_id INT,
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id),
    FOREIGN KEY (partner_id) REFERENCES partners(id)
);


INSERT INTO raw_materials_partners (raw_material_id, partner_id, props, enabled)
VALUES
    (1, 1, '{"key": "value1"}', 1),
    (2, 1, '{"key": "value2"}', 1),
    (3, 1, '{"key": "value2"}', 1),
    (4, 1, '{"key": "value2"}', 1),
    (5, 1, '{"key": "value2"}', 1),
    (6, 1, '{"key": "value2"}', 1),
    (7, 1, '{"key": "value2"}', 1),
    (8, 1, '{"key": "value2"}', 1),
    (9, 1, '{"key": "value2"}', 1),
    (10, 1, '{"key": "value2"}', 1),
    (11, 1, '{"key": "value2"}', 1),
    (12, 2, '{"key": "value2"}', 1),
    (13, 2, '{"key": "value2"}', 1),
    (14, 2, '{"key": "value2"}', 1),
    (15, 2, '{"key": "value2"}', 1),
    (16, 2, '{"key": "value2"}', 1),
    (17, 2, '{"key": "value3"}', 1);


CREATE TABLE bom (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    raw_material_id INT,
    quantity INT,
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id)
);


INSERT INTO bom (product_id, raw_material_id, quantity, props, enabled)
VALUES
    (1, 1, 3, '{"key": "value1"}', 1),
    (1, 2, 2, '{"key": "value2"}', 1),
    (1, 3, 1, '{"key": "value2"}', 1),
    (1, 4, 1, '{"key": "value2"}', 1),
    (1, 5, 1, '{"key": "value2"}', 1),
    (1, 6, 1, '{"key": "value2"}', 1),
    (1, 7, 2, '{"key": "value2"}', 1),
    (1, 8, 1, '{"key": "value2"}', 1),
    (1, 9, 1, '{"key": "value2"}', 1),
    (1, 10, 2, '{"key": "value2"}', 1),
    (1, 11, 2, '{"key": "value2"}', 1),
    (1, 12, 1, '{"key": "value2"}', 1);



CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    total DECIMAL(10, 2),
    props JSON,
    enabled BOOLEAN
);


INSERT INTO sales (date, total, props, enabled)
VALUES
    ('2023-01-15', 500.00, '{"key": "value1"}', 1),
    ('2023-02-20', 750.50, '{"key": "value2"}', 1),
    ('2023-03-25', 300.25, '{"key": "value3"}', 1);


CREATE TABLE products_sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    sale_id INT,
    quantity INT,
    subtotal DECIMAL(10, 2),
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (sale_id) REFERENCES sales(id)
);


INSERT INTO products_sales (product_id, sale_id, quantity, subtotal, props, enabled)
VALUES
    (1, 1, 2, 100.00, '{"key": "value1"}', 1),
    (1, 2, 3, 150.75, '{"key": "value2"}', 1),
    (2, 3, 1, 75.25, '{"key": "value3"}', 1);




