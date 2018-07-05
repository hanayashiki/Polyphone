
def summary(package):
    for key in package.data:
        print("%s: %d" % (key, len(package.data[key])))

if __name__ == '__main__':
    import resource.training_好
    summary(resource.training_好)