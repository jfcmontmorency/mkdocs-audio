import mkdocs
import lxml.html
from mkdocs.config import config_options
from mkdocs.exceptions import ConfigurationError

class Plugin(mkdocs.plugins.BasePlugin):
    config_scheme = (
        ("mark", config_options.Type(str, default="type:audio")),
        ("audio_type", config_options.Type(str, default="mp3")),
        ("audio_loop", config_options.Type(bool, default=False)),
        ("audio_controls", config_options.Type(bool, default=True)),
        ("audio_autoplay", config_options.Type(bool, default=False)),
        ("css_style", config_options.Type(
            dict,
            default={
                "position": "relative",
                "width": "100%",
                "height": "auto"
            }
        ))
    )

    def on_page_content(self, html, page, config, files):
        content = lxml.html.fromstring(html)
        tags = content.xpath(f'//img[@alt="{self.config["mark"]}" and @src]')
        for tag in tags:
            if not tag.attrib.get("src"):
                continue
            tag.getparent().replace(tag, self.create_repl_tag(tag))
        return lxml.html.tostring(content, encoding="unicode")

    def create_repl_tag(self, tag):
        """
        Create a replacement tag with the specified source and style.
        
        return: str
        """
        repl_tag = lxml.html.Element("audio")
        repl_tag.set("controls", "controls" if self.config["audio_controls"] else "")
        
        repl_subtag = lxml.html.Element("source")
        repl_subtag.set("src", tag.attrib["src"])
        audio_type = self.config["audio_type"].lower().strip()
        if any(i in audio_type for i in [" ", "/"]):
            raise ConfigurationError("Unsupported audio type")
        audio_type = f"audio/{audio_type}"
        repl_subtag.set("type", audio_type)
        repl_tag.append(repl_subtag)

        # Extended config if global is enabled
        if "disable-global-config" not in tag.attrib:
            css_style = ";".join(
                [f"{k}:{v}" for k, v in self.config["css_style"].items()]
            )
            repl_tag.set("style", css_style)

            if self.config["audio_loop"]:
                repl_tag.set("loop", "loop")
            if self.config["audio_autoplay"]:
                repl_tag.set("autoplay", "autoplay")
        else:
            tag.attrib.pop("disable-global-config")

        # Duplicate everything from original tag (except src)
        for attr, val in tag.attrib.items():
            if attr != "src":
                repl_tag.set(attr, val if val else None)

        div = lxml.html.Element("div")
        div.set("class", "audio-container")
        div.append(repl_tag)

        return div
