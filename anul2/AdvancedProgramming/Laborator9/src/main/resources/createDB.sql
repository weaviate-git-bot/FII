CREATE TABLE `continents` (
                              `id` int(11) NOT NULL,
                              `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `continents`
    ADD PRIMARY KEY (`id`);

ALTER TABLE `continents`
    MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

CREATE TABLE `countries` (
                             `id` int(11) NOT NULL,
                             `name` varchar(50) NOT NULL,
                             `code` varchar(10) NOT NULL,
                             `continent` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `countries`
    ADD PRIMARY KEY (`id`),
  ADD KEY `continent_fk` (`continent`);

ALTER TABLE `countries`
    MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `countries`
    ADD CONSTRAINT `continent_fk` FOREIGN KEY (`continent`) REFERENCES `continents` (`id`);
COMMIT;


CREATE TABLE `city` (
                        `id` int(11) NOT NULL,
                        `country` int(11) NOT NULL,
                        `name` varchar(255) NOT NULL,
                        `capital` tinyint(1) NOT NULL DEFAULT '0',
                        `latitude` double NOT NULL,
                        `longitude` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
ALTER TABLE `city`
    MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `city`
    ADD PRIMARY KEY (`id`),
  ADD KEY `city_fk` (`country`);

ALTER TABLE `city`
    ADD CONSTRAINT `city_fk` FOREIGN KEY (`country`) REFERENCES `countries` (`id`);
COMMIT;
