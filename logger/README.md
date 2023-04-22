## Usage
```python
import logger

log = logger.newLogger(__name__, logger.DEBUG)

log.info("Info")
log.debug("Debug")
log.error("Error")
log.fatal("Fatal")
```