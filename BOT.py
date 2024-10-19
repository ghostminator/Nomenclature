import tkinter as tk
from tkinter import ttk
import random

# Predefined lists of prefixes and suffixes
prefixes = ["data", "code", "byte", "info", "net", "algo", "tech", 
    "sys", "cloud", "script", "logic", "debug", "crypto", 
    "web", "dev", "auto", "multi", "nano", "hyper", "meta", 
    "quant", "pixel", "stream", "link", "api", "block", 
    "machine", "virtual", "cipher", "stack", "protocol", 
    "graph", "element", "widget", "token", "key", "json", 
    "xml", "frontend", "backend", "dynamic", "server", 
    "cache", "mesh", "cluster", "analytics", "binary", 
    "hash", "function", "schema", "repository", "pipeline", 
    "micro", "dataflow", "workflow", "engine", "component", 
    "module", "connector", "extractor", "transformer", 
    "validator", "aggregator", "scheduler", "initializer", 
    "processor", "monitor", "analyzer", "handler", "router", 
    "dispatcher", "factory", "observer", "controller", 
    "emitter", "store", "builder", "executor", "parser", 
    "compiler", "launcher", "navigator", "interpreter", 
    "sync", "batch", "object", "template", "query", 
    "service", "instance", "network", "packet", "socket", 
    "command", "task", "attribute", "type", "context", 
    "syntax", "source", "client", "bit", "factor", 
    "event", "field", "dimension", "async", "quantum", 
    "solid", "dynamic", "static", "eco", "bio", 
    "cyber", "geo", "astro", "tele", "inter", 
    "sub", "super", "trans", "retro", "cross", 
    "increment", "decrement", "forward", "reverse", "peer", 
    "self", "open", "closed", "flash", "output", 
    "input", "video", "audio", "session", "layout", 
    "fetch", "image", "compress", "encrypt", "process", 
    "access", "connect", "deploy", "path", "filter", 
    "job", "trace", "capture", "matrix", "file", 
    "result", "storage", "request", "word", "row", 
    "column", "block", "item", "copy", "url", 
    "test", "retry", "log", "report", "address", 
    "structure", "value", "record", "database", "point", 
    "connection", "bandwidth", "focus", "strategy", 
    "summary", "intelligence", "security", "index", "status", 
    "sequence", "scenario", "version", "solution", "synchronization", 
    "collaboration", "share", "distribution", "extension", 
    "configuration", "analysis", "specification", "model", 
    "definition", "response", "chain", "level", "operation", 
    "validation", "array", "class", "set", "service", 
    "product", "step", "name", "program", "control", 
    "channel", "user", "identity", "authentication", 
    "authorization", "resource", "performance", "identifier", 
    "comparison", "feedback", "communication", "form", "rule", 
    "method", "expression", "transmission", "return", "condition", 
    "schedule", "encryption", "assignment", "question", 
    "statement", "language", "header", "check", 
    "operation", "team", "document", "signature", 
    "device", "browser", "history", "state", "page", 
    "manager", "application", "library", "default", 
    "message", "execution", "call", "string", "id", 
    "base", "change", "relation", "event", "action", 
    "loop", "flow", "value", "plan", "container", 
    "field", "module", "snapshot", "history", "setting", 
    "verification", "automation", "monitoring", "property", 
    "variable", "constraint", "indicator", "timeline", 
    "tag", "signal", "structure", "name", "section", 
    "limit", "pattern", "node", "queue", "link", 
    "file", "index", "command", "task", "option", 
    "counter", "profile", "group", "filter", "step", 
    "security", "style", "transaction", "matrix", 
    "name", "point", "script", "line", "list", 
    "chain", "location", "parameter", "result", "state", 
    "report", "time", "queue", "action", "rule", 
    "manager", "element", "instance", "log", "definition", 
    "item", "service", "table", "history", "queue", 
    "task", "status", "condition", "tag", "definition", 
    "snapshot", "filter", "view", "object", 
    "plan", "schedule", "action", "operation", "result", 
    "schema", "column", "state", "list", "task", 
    "test", "resource", "key", "group", "statement", 
    "output", "job", "status", "flow", "action", 
    "execution", "line", "parameter", "plan", "entry", 
    "state", "object", "component", "history", "operation", 
    "group", "job", "status", "item",]
suffixes = [
    "node", "task", "box", "path", "list", "view", "set",
    "point", "log", "key", "data", "type", "obj", "file",
    "stream", "unit", "service", "flag", "state", "count",
    "map", "chain", "link", "info", "field", "job", "task",
    "mode", "cache", "queue", "index", "form", "rule",
    "graph", "event", "port", "value", "code", "tag",
    "pair", "rate", "base", "entry", "block", "point",
    "stream", "config", "plan", "session", "scope", "fetch",
    "check", "filter", "handler", "option", "module", "frame",
    "pattern", "batch", "signal", "signal", "marker", "loop",
    "group", "time", "link", "name", "layer", "field",
    "chain", "point", "type", "id", "block", "string",
    "case", "param", "step", "source", "method", "event",
    "count", "color", "rate", "component", "plugin", "source",
    "range", "filter", "process", "class", "check", "plan",
    "store", "key", "anchor", "wrapper", "label", "wrapper",
    "metric", "trace", "root", "spec", "scope", "value",
    "access", "anchor", "rule", "tracker", "session", "pointer",
    "outcome", "provider", "header", "spec", "reference", "task",
    "selector", "group", "matrix", "provider", "action", "query",
    "phase", "view", "buffer", "input", "user", "rate",
    "trigger", "aspect", "instance", "data", "factory", "pack",
    "packet", "store", "slice", "key", "host", "config",
    "status", "output", "checkpoint", "response", "device", "endpoint",
    "container", "handler", "request", "service", "processor", 
    "adapter", "template", "schema", "validator", "analyzer", 
    "builder", "executor", "publisher", "subscriber", "consumer", 
    "provider", "connector", "adapter", "configuration", "manager", 
    "registry", "controller", "executor", "reporter", "inspector", 
    "middleware", "listener", "parser", "scheduler", "iterator", 
    "handler", "renderer", "modifier", "scheduler", "loader", 
    "synchronizer", "expander", "wrapper", "collector", "navigator", 
    "updater", "initializer", "dumper", "crawler", "viewer", 
    "filter", "observer", "iterator", "selector", "streamer", 
    "transmitter", "exporter", "importer", "normalizer", "comparator", 
    "transformer", "serializer", "deserializer", "router", "dispatcher", 
    "actor", "speaker", "sender", "receiver", "monitor", 
    "logger", "tracer", "scout", "explorer", "patch", 
    "helper", "assistant", "function", "module", "partner", 
    "instance", "cluster", "batch", "result", "alert", 
    "limit", "matrix", "snapshot", "checkpoint", "version", 
    "counter", "status", "meta", "processor", "status", 
    "engine", "path", "configuration", "template", "modifier", 
    "builder", "profile", "key", "log", "sample", 
    "row", "set", "score", "deck", "style", 
    "map", "point", "pair", "cursor", "track"
]

generated_names = set()  # Set to track generated names

class NameGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Name Generator")
        self.root.geometry("250x150")  # Compact window size
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        """Create and place all widgets in the application."""
        self.main_frame = tk.Frame(self.root, bg="#121212", padx=10, pady=10)
        self.main_frame.pack(fill='both', expand=True)

        self.title_label = tk.Label(
            self.main_frame, 
            text="Name Generator", 
            font=("Helvetica", 14, "bold"), 
            bg="#121212", 
            fg="#ffffff"
        )
        self.title_label.pack(pady=(5, 5))

        # Compact output box
        self.name_text = tk.Text(
            self.main_frame, 
            font=("Helvetica", 12), 
            wrap='word', 
            height=1, 
            bd=0, 
            highlightthickness=0, 
            bg="#212121", 
            fg="#ffffff", 
            relief="flat"
        )
        self.name_text.pack(expand=True, fill='x', pady=(0, 10))
        self.name_text.config(state=tk.DISABLED)

        # Stylish frame for buttons
        self.button_frame = tk.Frame(self.main_frame, bg="#121212")
        self.button_frame.pack(pady=5)

        # Generate name button
        self.generate_button = ttk.Button(
            self.button_frame, 
            text="Generate", 
            command=self.generate_name, 
            width=10
        )
        self.generate_button.pack(pady=5)

        # Customize button style for a modern look
        style = ttk.Style()
        style.configure("TButton", 
                        background="#ff5722", 
                        foreground="#ffffff", 
                        font=("Helvetica", 10, "bold"),
                        padding=5)
        style.map("TButton", 
                  background=[("active", "#e64a19")], 
                  relief=[("pressed", "flat"), ("!pressed", "raised")])

        # Add a subtle shadow effect to the button
        self.add_shadow_effect(self.generate_button)

    def add_shadow_effect(self, button):
        """Create a shadow effect for the button."""
        button.bind("<Enter>", lambda e: button.config(relief="raised"))
        button.bind("<Leave>", lambda e: button.config(relief="flat"))

    def generate_name(self):
        """Generate a random name based on predefined prefixes and suffixes."""
        if len(generated_names) >= len(prefixes) * len(suffixes):
            self.name_text.config(state=tk.NORMAL)
            self.name_text.delete(1.0, tk.END)
            self.name_text.insert(tk.END, "I RAN OUT SON!")
            self.name_text.config(state=tk.DISABLED)
            return

        while True:
            prefix = random.choice(prefixes)
            suffix = random.choice(suffixes)
            name = f"{prefix}{suffix}"

            if name not in generated_names:
                generated_names.add(name)
                break

        # Display the generated name
        self.name_text.config(state=tk.NORMAL)
        self.name_text.delete(1.0, tk.END)
        self.name_text.insert(tk.END, name)
        self.name_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NameGeneratorApp(root)
    root.mainloop()
