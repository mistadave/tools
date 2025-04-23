# Kubernetes

## BusyBox

Example sarting a busy box plain and one which attaches to a volume calles `trendz-data`.

```bash
# Plain busy box
kubectl run -i --rm --tty busybox --image=busybox --restart=Never -- sh
# Attach volume trendz-data
kubectl run -i --rm --tty busybox --overrides='
{
    "apiVersion": "v1",
    "kind": "Pod",
    "spec": {
        "containers": [
            {
                "args": [
                    "sh"
                ],
                "image": "busybox",
                "imagePullPolicy": "Always",
                "name": "busybox",
                "stdin": true,
                "stdinOnce": true,
                "tty": true,
                "volumeMounts": [
                    {
                        "mountPath": "/data",
                        "name": "trendz-data"
                    }
                ],
                "priority": 0,
                "restartPolicy": "Never"
            }
        ],
        "volumes": [
            {
                "name": "trendz-data",
                "persistentVolumeClaim": {
                    "claimName": "trendz-data"
                }
            }
        ]
    }
}
' --image=busybox --restart=Never -- sh
```
