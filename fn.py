def fn():
    print('<fn>')
    print('</fn>')

def main():
    print('<main>')
    fn()
    print('</main>')

if __name__== '__main__':
    import ipdb; ipdb.set_trace()
    print('<outside>')
    main()
    print('</outside>')
