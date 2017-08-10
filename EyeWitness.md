# EyeWitness -a Websites Screenshots Tool
Repository site: [https://github.com/ChrisTruncer/EyeWitness](https://github.com/ChrisTruncer/EyeWitness)

## Usage 

### build
```
git clone https://github.com/ChrisTruncer/EyeWitness
cd EyeWitness
docker build -t image_name .
```

### run
```
docker run --rm -it -v /tmp/EyeWitness:/tmp/EyeWitness vulhub/eyewitness -f /tmp/EyeWitness/input.txt --headless
```
