from prometheus_client import Counter

REQUEST_COUNTER = Counter(

    "requests",

    "Total API Requests"

)