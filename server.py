import runpod

def handler(job): prompt = job["input"].get("prompt", "")

return { "response": f"AurX a reçu : {prompt}" } 

runpod.serverless.start({ "handler": handler })

