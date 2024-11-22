import fake_useragent
import logging
from logging import FileHandler, Formatter
'''
Config file for DEX Screener parser.
'''


# region Request config.
url = 'https://api.dexscreener.com/token-boosts/latest/v1'  # get latest boosts tokens
user_agent = fake_useragent.UserAgent().random
headers = {
    'user-agent': user_agent
}
proxies = dict()
# endregion
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

#region Setting up logger.
logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = FileHandler(filename='./logs.txt')
handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
logger.addHandler(handler)
#endregion

