"""
Copyright © 2021 by 1Silverbullet.tech
All rights reserved.
No part of this code may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, 
 recording or other electronic or mechanical methods

Maintainer: 1SilverBullet Tech

"""

import uuid
from starlette.responses import JSONResponse
def responseModel(statusCode, errors=[], data={}, requestId = ""):
    if requestId == "":
        requestId = str(uuid.uuid4())
    obj = {
        "reqId": requestId,
        "errors": errors,
        "data": data
    }
    return JSONResponse(status_code=statusCode, content=obj)