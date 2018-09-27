
-- Basic data
INSERT INTO vacancy (vacancy, salary, experience, city) VALUES ('Big Data Engineer', 180000, 4, 'Москва');
INSERT INTO vacancy (vacancy, salary, experience, city) VALUES ('Старший разработчик Python', 180000, 7, 'Санкт-Петербург');
INSERT INTO vacancy (vacancy, salary, experience, city) VALUES ('CTO', 250000, 7, 'Санкт-Петербург');

-- Roles
INSERT INTO role (role, password) VALUES ('viewer', 'viewerpassword'), ('editor', 'editorpassword');

-- Permissions
WITH s AS (SELECT id, role FROM role) INSERT INTO access (id, resource) VALUES 
((SELECT id FROM s WHERE role = 'viewer'), 'listitems'),
((SELECT id FROM s WHERE role = 'viewer'), 'getitem'),
((SELECT id FROM s WHERE role = 'editor'), 'listitems'),
((SELECT id FROM s WHERE role = 'editor'), 'getitem'),
((SELECT id FROM s WHERE role = 'editor'), 'additem'),
((SELECT id FROM s WHERE role = 'editor'), 'removeitem');