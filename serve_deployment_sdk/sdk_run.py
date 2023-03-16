from ray import serve
from file import MyRun
import ray


@serve.deployment(num_replicas=1)
class RunCode:

    def __int__(self, input: int):
        if not ray.is_initialized():
            runtime_env = {"env_vars": {"TF_WARNINGS": "none"},
                           "working_dir": "./",
                           "excludes": ["*core*", "*.git*"]
                           }
            ray.init("auto", runtime_env=runtime_env, _metrics_export_port=8080)
            print("Ray started")
            self.input = input

    def __call__(self, *args, **kwargs):
        obj = MyRun()
        obj.run()


sdk = RunCode.bind(5)