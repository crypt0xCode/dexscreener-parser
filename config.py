import fake_useragent
from loguru import logger
'''
Config file for DEX Screener parser.
'''


#region Constants.
ALL_TOKENS_FILE_PATH: str = './tokens.json'
TOKENS_INFO_FOLDER_FILE_PATH: str = './tokens-info/'
LATENCY: int = 60 # change this constant for faster or slower API GET requests
LOGS_PATH: str = './logs.log'
LOGO: str = '''

                                                                                                                                                                                                 dddddddd                    
                                                                                           tttt               000000000                                CCCCCCCCCCCCC                             d::::::d                    
                                                                                        ttt:::t             00:::::::::00                           CCC::::::::::::C                             d::::::d                    
                                                                                        t:::::t           00:::::::::::::00                       CC:::::::::::::::C                             d::::::d                    
                                                                                        t:::::t          0:::::::000:::::::0                     C:::::CCCCCCCC::::C                             d:::::d                     
    ccccccccccccccccrrrrr   rrrrrrrrryyyyyyy           yyyyyyyppppp   ppppppppp   ttttttt:::::ttttttt    0::::::0   0::::::0xxxxxxx      xxxxxxxC:::::C       CCCCCC   ooooooooooo       ddddddddd:::::d     eeeeeeeeeeee    
  cc:::::::::::::::cr::::rrr:::::::::ry:::::y         y:::::y p::::ppp:::::::::p  t:::::::::::::::::t    0:::::0     0:::::0 x:::::x    x:::::xC:::::C               oo:::::::::::oo   dd::::::::::::::d   ee::::::::::::ee  
 c:::::::::::::::::cr:::::::::::::::::ry:::::y       y:::::y  p:::::::::::::::::p t:::::::::::::::::t    0:::::0     0:::::0  x:::::x  x:::::x C:::::C              o:::::::::::::::o d::::::::::::::::d  e::::::eeeee:::::ee
c:::::::cccccc:::::crr::::::rrrrr::::::ry:::::y     y:::::y   pp::::::ppppp::::::ptttttt:::::::tttttt    0:::::0 000 0:::::0   x:::::xx:::::x  C:::::C              o:::::ooooo:::::od:::::::ddddd:::::d e::::::e     e:::::e
c::::::c     ccccccc r:::::r     r:::::r y:::::y   y:::::y     p:::::p     p:::::p      t:::::t          0:::::0 000 0:::::0    x::::::::::x   C:::::C              o::::o     o::::od::::::d    d:::::d e:::::::eeeee::::::e
c:::::c              r:::::r     rrrrrrr  y:::::y y:::::y      p:::::p     p:::::p      t:::::t          0:::::0     0:::::0     x::::::::x    C:::::C              o::::o     o::::od:::::d     d:::::d e:::::::::::::::::e 
c:::::c              r:::::r               y:::::y:::::y       p:::::p     p:::::p      t:::::t          0:::::0     0:::::0     x::::::::x    C:::::C              o::::o     o::::od:::::d     d:::::d e::::::eeeeeeeeeee  
c::::::c     ccccccc r:::::r                y:::::::::y        p:::::p    p::::::p      t:::::t    tttttt0::::::0   0::::::0    x::::::::::x    C:::::C       CCCCCCo::::o     o::::od:::::d     d:::::d e:::::::e           
c:::::::cccccc:::::c r:::::r                 y:::::::y         p:::::ppppp:::::::p      t::::::tttt:::::t0:::::::000:::::::0   x:::::xx:::::x    C:::::CCCCCCCC::::Co:::::ooooo:::::od::::::ddddd::::::dde::::::::e          
 c:::::::::::::::::c r:::::r                  y:::::y          p::::::::::::::::p       tt::::::::::::::t 00:::::::::::::00   x:::::x  x:::::x    CC:::::::::::::::Co:::::::::::::::o d:::::::::::::::::d e::::::::eeeeeeee  
  cc:::::::::::::::c r:::::r                 y:::::y           p::::::::::::::pp          tt:::::::::::tt   00:::::::::00    x:::::x    x:::::x     CCC::::::::::::C oo:::::::::::oo   d:::::::::ddd::::d  ee:::::::::::::e  
    cccccccccccccccc rrrrrrr                y:::::y            p::::::pppppppp              ttttttttttt       000000000     xxxxxxx      xxxxxxx       CCCCCCCCCCCCC   ooooooooooo      ddddddddd   ddddd    eeeeeeeeeeeeee  
                                           y:::::y             p:::::p                                                                                                                                                       
                                          y:::::y              p:::::p                                                                                                                                                       
                                         y:::::y              p:::::::p                                                                                                                                                      
                                        y:::::y               p:::::::p                                                                                                                                                      
                                       yyyyyyy                p:::::::p                                                                                                                                                      
                                                              ppppppppp                                                                                                                                                      



'''
#endregion

#region Loguru config.
logger.add(
    LOGS_PATH,
    level='DEBUG'
)
#endregion

#region Request config.
token_boosts_url: str = 'https://api.dexscreener.com/token-boosts/latest/v1'  # get latest boosts tokens

token_address: str = ''
token_info_url: str = f'https://api.dexscreener.com/latest/dex/tokens/{token_address}'

user_agent = fake_useragent.UserAgent().random
headers = {
    'user-agent': user_agent
}
proxies = dict()
#endregion


def set_token_address(address: str = '') -> None:
    """
    Set specify token address.
    :param address: token address.
    :return: None.
    """
    global token_address
    token_address = address
    update_token_info_url()


def update_token_info_url() -> None:
    """
    Update token info API request.
    :return: None.
    """
    global token_info_url
    token_info_url = f'https://api.dexscreener.com/latest/dex/tokens/{token_address}'


#region Tokens .json config.
fp_token_name: str = ''
current_token_file_path: str = f'{fp_token_name}.json'


def set_token_name(name: str = '') -> None:
    """
    Set specify token name for JSON data.
    :param name: token name.
    :return: None.
    """
    global fp_token_name
    if '/' in name:
        name = name.replace('/', '_')
    fp_token_name= name
    update_current_token_file_path()


def update_current_token_file_path() -> None:
    """
    Update filepath for current token JSON data.
    :return: None.
    """
    global current_token_file_path
    current_token_file_path= f'{fp_token_name}.json'
#endregion