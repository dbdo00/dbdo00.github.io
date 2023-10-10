import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

class IgnoreSectionExtension(Extension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(IgnoreSectionPreprocessor(md), "ignore_section", 1)

class IgnoreSectionPreprocessor(Preprocessor):
    def run(self, lines):
        # Initialize a variable to store the ignored content
        ignored_content = []

        # Find the start and end markers
        start_marker = "---"
        end_marker = "---"
        in_ignored_section = False

        # Iterate through the lines and ignore the content
        for line in lines:
            if line.strip() == start_marker:
                in_ignored_section = not in_ignored_section
            elif in_ignored_section:
                ignored_content.append(line)
            else:
                yield line

        # Expose the ignored content as a variable (You can customize this part)
        self.md.ignored_content = "\n".join(ignored_content)

def makeExtension(*args, **kwargs):
    return IgnoreSectionExtension(*args, **kwargs)

