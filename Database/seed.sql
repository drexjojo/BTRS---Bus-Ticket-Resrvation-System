-- INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
-- (1, 'Can add log entry', 1, 'add_logentry'),
-- (2, 'Can change log entry', 1, 'change_logentry'),
-- (3, 'Can delete log entry', 1, 'delete_logentry'),
-- (4, 'Can add permission', 2, 'add_permission'),
-- (5, 'Can change permission', 2, 'change_permission'),
-- (6, 'Can delete permission', 2, 'delete_permission'),
-- (7, 'Can add group', 3, 'add_group'),
-- (8, 'Can change group', 3, 'change_group'),
-- (9, 'Can delete group', 3, 'delete_group'),
-- (10, 'Can add user', 4, 'add_user'),
-- (11, 'Can change user', 4, 'change_user'),
-- (12, 'Can delete user', 4, 'delete_user'),
-- (13, 'Can add content type', 5, 'add_contenttype'),
-- (14, 'Can change content type', 5, 'change_contenttype'),
-- (15, 'Can delete content type', 5, 'delete_contenttype'),
-- (16, 'Can add session', 6, 'add_session'),
-- (17, 'Can change session', 6, 'change_session'),
-- (18, 'Can delete session', 6, 'delete_session'),
-- (19, 'Can add bus pick area', 7, 'add_buspickarea'),
-- (20, 'Can change bus pick area', 7, 'change_buspickarea'),
-- (21, 'Can delete bus pick area', 7, 'delete_buspickarea'),
-- (22, 'Can add bus drop area', 8, 'add_busdroparea'),
-- (23, 'Can change bus drop area', 8, 'change_busdroparea'),
-- (24, 'Can delete bus drop area', 8, 'delete_busdroparea'),
-- (25, 'Can add bus info', 9, 'add_businfo'),
-- (26, 'Can change bus info', 9, 'change_businfo'),
-- (27, 'Can delete bus info', 9, 'delete_businfo'),
-- (28, 'Can add book aticket', 10, 'add_bookaticket'),
-- (29, 'Can change book aticket', 10, 'change_bookaticket'),
-- (30, 'Can delete book aticket', 10, 'delete_bookaticket');

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$24000$6f63EyYtOwBp$Q8xRFwAn+Vo6EGoP9eoHNIEqJlX9oC/LiGNrmW45iIY=', '2016-03-24 14:51:30.970934', 1, 'bus_admin', '', '', 'bus@gmail.com', 1, 1, '2016-03-11 19:21:56.105143'),
(2, 'pbkdf2_sha256$24000$KyetaLZWY0Uw$GQLJV0yz33MfPWQbRSBqVWvTlcoA1+TffG6RMEGqJv0=', '2016-03-19 20:49:02.590413', 0, 'andy', '', '', '', 0, 1, '2016-03-17 17:50:56.807446'),
(3, 'pbkdf2_sha256$24000$1NjzqqWkc4Ed$t+aGlg7EVsIEocTn+R994W8JOFIktmYgluYNikoWtws=', '2016-03-17 17:53:27.229433', 0, 'niki', '', '', '', 0, 1, '2016-03-17 17:53:26.437388'),
(4, 'pbkdf2_sha256$24000$jK3YRS8uu9nP$prrQ5ONDLaxyFOACFOFrTrOm3NNQ9dQZ3cUL0YBtmxw=', '2016-03-20 16:26:05.177169', 0, 'nikichiki', '', '', '', 0, 1, '2016-03-19 15:09:30.251371');



-- INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
-- (1, '2016-03-11 19:25:34.088611', '1', 'Borivali(east)', 1, 'Added.', 7, 1),
-- (2, '2016-03-11 19:25:41.478034', '2', 'Vasai', 1, 'Added.', 7, 1),
-- (3, '2016-03-11 19:26:45.637704', '1', 'Karjat', 1, 'Added.', 8, 1),
-- (4, '2016-03-11 19:27:06.091873', '2', 'Swargate(pune)', 1, 'Added.', 8, 1),
-- (5, '2016-03-11 19:35:51.436921', '1', 'Niki Bus', 1, 'Added.', 9, 1),
-- (6, '2016-03-14 17:07:01.451745', '2', 'Jyoti travels', 1, 'Added.', 9, 1),
-- (7, '2016-03-14 18:01:06.892988', '2', 'Jyoti travels', 2, 'Changed depature_time.', 9, 1),
-- (8, '2016-03-14 18:18:25.895609', '1', 'Niki Bus Travels', 2, 'Changed bus_name.', 9, 1),
-- (9, '2016-03-19 15:57:29.133909', '2', 'BUSBK#002', 2, 'Changed status.', 10, 1),
-- (10, '2016-03-19 20:48:40.101574', '2', 'andy', 2, 'Changed password.', 4, 1),
-- (11, '2016-03-20 16:25:48.180197', '4', 'BUSBK#004', 2, 'Changed status.', 10, 1);

INSERT INTO `Route` (`id`, `route_name`, `slug`,`is_available`, `created_at`, `updated_at`) VALUES
(1,'Gachibowli','Gachibowli','1', '2016-03-11 19:25:33.957604', '2016-03-11 19:25:33.957604'),
(2,'HiTech','HiTech','1', '2016-03-11 19:25:33.957604', '2016-03-11 19:25:33.957604'),
(3,'Jubliee','Jubliee','1', '2016-03-11 19:25:33.957604', '2016-03-11 19:25:33.957604');

INSERT INTO `Stop` (`id`, `area_name`, `slug`, `created_at`, `updated_at`,`route_id`) VALUES
(1, 'A', 'A', '2016-03-11 19:25:33.957604', '2016-03-11 19:25:33.957604','1'),
(2, 'B', 'B', '2016-03-11 19:25:41.455032', '2016-03-11 19:25:41.455032','1'),
(3, 'C', 'C', '2016-03-11 14:26:45.624703', '2016-03-11 19:26:45.624703','1'),
(4, 'D', 'D', '2016-03-11 19:27:06.075873', '2016-03-11 19:27:06.075873','1'),
(6, 'F', 'F', '2016-03-11 13:27:06.075873', '2016-03-11 19:27:06.075873','1'),
(7, 'G', 'G', '2016-03-11 11:37:06.075873', '2016-03-11 19:27:06.075873','1'),

(9, 'I', 'I', '2016-03-11 19:37:06.075873', '2016-03-11 19:27:06.075873','2'),
(10, 'J', 'J', '2016-03-11 19:21:06.075873', '2016-03-11 19:27:06.075873','2'),
(11, 'B', 'Bb', '2016-03-11 19:25:41.455032', '2016-03-11 19:25:41.455032','2'),
(12, 'C', 'Cc', '2016-03-11 14:26:45.624703', '2016-03-11 19:26:45.624703','2'),

(5, 'E', 'E', '2016-03-11 14:27:06.075873', '2016-03-11 19:27:06.075873','3'),
(8, 'H', 'H', '2016-03-11 19:25:06.075873', '2016-03-11 19:27:06.075873','3'),
(13, 'D', 'Dd', '2016-03-11 19:27:06.075873', '2016-03-11 19:27:06.075873','3'),
(14, 'J', 'Jj', '2016-03-11 19:21:06.075873', '2016-03-11 19:27:06.075873','3');





-- INSERT INTO `busrv_busDropArea` (`id`, `area_name`, `slug`, `created_at`, `updated_at`) VALUES
-- (1, 'Karjat', 'karjat', '2016-03-11 19:26:45.624703', '2016-03-11 19:26:45.624703'),
-- (2, 'Swargate(pune)', 'swargatepune', '2016-03-11 19:27:06.075873', '2016-03-11 19:27:06.075873');

INSERT INTO `Bus` (`id`, `bus_number`, `slug`, `type`, `arriving_time`, `depature_time`, `fare`, `no_of_seats`, `is_active`, `created_at`, `updated_at`, `image`, `arriving_from_id`, `depature_at_id`) VALUES
(1, 1, 'niki-bus', 'AC', '18:00:00.000000', '18:05:00.000000', '300.00', 43, 1, '2016-03-11 19:35:51.355917', '2016-03-14 18:18:25.710599', 'images/bus/main/volvo1.jpg', 1, 2),
(2, 1, 'niki-bus1', 'AC', '18:05:00.000000', '18:15:00.000000', '300.00', 43, 1, '2016-03-11 19:35:51.355917', '2016-03-14 18:18:25.710599', 'images/bus/main/volvo1.jpg', 2, 3),
(3, 1, 'niki-bus2', 'AC', '18:15:00.000000', '18:20:00.000000', '300.00', 43, 1, '2016-03-11 19:35:51.355917', '2016-03-14 18:18:25.710599', 'images/bus/main/volvo1.jpg', 3,4),
(4, 1, 'niki-bus3', 'AC', '18:20:00.000000', '18:30:00.000000', '300.00', 43, 1, '2016-03-11 19:35:51.355917', '2016-03-14 18:18:25.710599', 'images/bus/main/volvo1.jpg', 4, 6),
(5, 1, 'niki-bus4', 'AC', '18:30:00.000000', '18:45:00.000000', '300.00', 43, 1, '2016-03-11 19:35:51.355917', '2016-03-14 18:18:25.710599', 'images/bus/main/volvo1.jpg', 6, 7),

(6, 2, 'jyoti-travels', 'AC', '19:00:00.000000', '19:03:00.000000', '500.00', 50, 1, '2016-03-14 17:07:00.968717', '2016-03-14 18:01:06.644974', 'images/bus/main/1662227372_v1.jpg', 11, 12),
(7, 2, 'jyoti-travels1', 'AC', '19:03:00.000000', '19:07:00.000000', '500.00', 50, 1, '2016-03-14 17:07:00.968717', '2016-03-14 18:01:06.644974', 'images/bus/main/1662227372_v1.jpg', 12, 10),
(8, 2, 'jyoti-travels2', 'AC', '19:07:00.000000', '19:15:00.000000', '500.00', 50, 1, '2016-03-14 17:07:00.968717', '2016-03-14 18:01:06.644974', 'images/bus/main/1662227372_v1.jpg', 10, 9),

(9, 3, 'allen-travels3', 'NAC', '19:30:00.000000', '19:33:00.000000', '500.00', 50, 1, '2016-03-14 17:07:00.968717', '2016-03-14 18:01:06.644974', 'images/bus/main/1662227372_v1.jpg', 5, 13),
(10, 3, 'allen-travels4', 'NAC', '19:33:00.000000', '19:38:00.000000', '500.00', 50, 1, '2016-03-14 17:07:00.968717', '2016-03-14 18:01:06.644974', 'images/bus/main/1662227372_v1.jpg', 13, 8),
(11, 3, 'allen-travels5', 'NAC', '19:38:00.000000', '19:42:00.000000', '500.00', 50, 1, '2016-03-14 17:07:00.968717', '2016-03-14 18:01:06.644974', 'images/bus/main/1662227372_v1.jpg', 8, 14);



INSERT INTO `bookTicket_bookaticket` (`id`, `booking_date`, `status`, `ip_address`, `last_updated`, `date`, `email`, `phone`, `booking_seats_num`, `fare`, `bus_id`, `user_id`) VALUES
(1, '2016-03-17 18:30:00.000000', 'P', '127.0.0.1', '2016-03-17 17:14:08.402827', '2016-03-17 17:14:08.402827', 'aniruddha@gmail.com', '9978675678', 4, '500.00', 2, 1),
(2, '2016-03-17 18:30:00.000000', 'C', '127.0.0.1', '2016-03-19 15:57:29.083906', '2016-03-17 17:21:10.925255', 'aniruddha@gmail.com', '9948584235', 5, '500.00', 2, 1),
(3, '2016-03-25 18:30:00.000000', 'P', '127.0.0.1', '2016-03-19 20:43:54.148685', '2016-03-19 20:43:54.148685', 'niki@gmail.com', '9945654565', 2, '300.00', 1, 4),
(4, '2016-03-20 18:30:00.000000', 'C', '127.0.0.1', '2016-03-20 16:25:48.154196', '2016-03-20 16:21:15.411596', 'nikimadgirl@item.com', '9920755049', 3, '300.00', 1, 4);
