from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()
USER = os.environ.get("ROOT_USER")
PASSWORD = os.environ.get("ROOT_PASSWORD")
DB_NAME = os.environ.get("DATABASE_NAME")
HOST = "localhost"

Base = automap_base()
print(f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")
engine = create_engine(f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")
Base.prepare(engine, reflect=True)

User = Base.classes.user

"""
create table hazlnut_prod.user
(
    userid            bigint auto_increment
        primary key,
    username          text                                          not null,
    email             text                                          not null,
    password          text                                          not null,
    password2         varchar(256)                                  null,
    salt              varchar(32)                                   null,
    failedAttempts    int(5)          default 0                     not null,
    zipcode           varchar(10)                                   null,
    dob               varchar(100)                                  null,
    joindate          datetime        default '0000-00-00 00:00:00' not null,
    bank              text                                          not null,
    wallet            bigint                                        not null,
    totalearnedpoints bigint          default 0                     not null,
    acctpermissions   enum ('1', '0') default '1'                   not null,
    isadmin           enum ('0', '1') default '0'                   not null,
    emailtoken        varchar(200)    default ''                    null,
    isactive          enum ('0', '1') default '0'                   not null,
    isGuest           enum ('0', '1') default '0'                   not null,
    onNotification    enum ('1', '0') default '1'                   not null,
    eligible          enum ('0', '1') default '1'                   not null,
    chatEligible      enum ('1', '0') default '1'                   not null,
    photoAssist       enum ('0', '1') default '1'                   not null,
    firstName         varchar(25)                                   null,
    lastName          varchar(25)                                   null,
    gender            varchar(25)                                   null,
    phone             varchar(15)                                   null,
    age_range_min     varchar(5)                                    null,
    age_range_max     varchar(5)                                    null,
    aggrID            bigint                                        null,
    source            varchar(128)    default 'gng rater'           null,
    partnerID         bigint                                        null,
    caAdmin           tinyint(1)      default 0                     not null,
    newInstall        tinyint(1)      default 0                     null,
    phoneValidated    tinyint(1)      default 0                     not null,
    updatedOn         timestamp       default CURRENT_TIMESTAMP     not null on update CURRENT_TIMESTAMP
)
    charset = utf8;

create index id_user_email
    on hazlnut_prod.user (email(20));

create index id_user_username
    on hazlnut_prod.user (username(20));

create index partnerID
    on hazlnut_prod.user (partnerID);

create index userID_source
    on hazlnut_prod.user (userid, source);


"""



