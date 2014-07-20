drop table if exists news_feeds;
create table news_feeds(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title UNICODETEXT,
        title_hash UNICODETEXT,
        filename UNICODETEXT,
        timestamp datetime
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists news_tags;
create table news_tags (
        news_id INTEGER,
        tag_id INTEGER
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists tags;
create table tags (
        id INTEGER AUTOINCREMENT,
        title UNICODETEXT,
        PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
