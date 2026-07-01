from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Enterprise Finance Server")


@mcp.tool()

def portfolio_summary():

    return {

        "Portfolio Value": "$150 Million",

        "VaR": "$2.3 Million"

    }


@mcp.tool()

def stress_test():

    return {

        "Scenario": "Market Crash",

        "Loss": "-8.5%"

    }


if __name__ == "__main__":

    mcp.run()