
----------------------
-- "Vacancy" entity
----------------------

CREATE TABLE vacancy (
  id SERIAL NOT NULL,           -- ID (P)
  vacancy VARCHAR(32) NOT NULL, -- Name
  salary INT,                   -- Salary
  experience INT,               -- Required experience
  city VARCHAR(32),             -- City
  PRIMARY KEY (id)
);

CREATE INDEX ON vacancy (vacancy);
CREATE INDEX ON vacancy (salary);
CREATE INDEX ON vacancy (experience);
CREATE INDEX ON vacancy (city);


----------------------
-- "Role" entity
----------------------

CREATE TABLE role (
  id SERIAL NOT NULL,           -- ID (P)
  role VARCHAR(32) NOT NULL,    -- Role (U)
  password VARCHAR(32),         -- Password
  PRIMARY KEY(id),
  UNIQUE(role)
);

CREATE INDEX ON role (role, password);


----------------------
-- "Access rights" entity
----------------------

CREATE TABLE access (
  id INT NOT NULL REFERENCES role(id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE,  -- Role identifier (=>Role.id)
  resource VARCHAR(16) NOT NULL,   -- Handler/Resource
  PRIMARY KEY (id, resource)
);
