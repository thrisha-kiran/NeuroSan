from neuro_san.tools.base_tool import BaseTool

class HelloTool(BaseTool):
    name = "hello_tool"
    description = "Returns a friendly greeting"

    def run(self, user_input: str) -> str:
        return f"Hello! You said: {user_input}"

