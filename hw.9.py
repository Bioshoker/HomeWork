# Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег (например: <tag></tag>).
# От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение:
# Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через img = Image(),
# а через фабричный метод или фабрику, например factory.create_tag(name).


class TagFactory:
    def __init__(self):
        pass

    def create_tag(self, tag, *args, **kwargs):
        created_tag = self._create_tag(tag, args, kwargs)
        return created_tag

    def _create_tag(self, tag, *args, **kwargs):
        if tag == 'image':
            src = input('Enter src for image tag: ')
            return Image(tag, src)
        elif tag == 'p':
            content = input('Enter content for text tag: ')
            return Text(tag, content)
        elif tag == 'input':
            return Input(tag)
        elif tag == 'a':
            href = input('Enter href for link tag: ')
            content = input('Enter content for link tag: ')
            return Link(tag, href, content)
        else:
            raise ValueError('that kind of tags is not supported yet')


class Tag:
    def __init__(self, name, *args, **kwargs):
        print('creating new tag {}'.format(name))
        self.name = name
        self.tag = ''

    def get_html(self):
        return "<{0}></{0}>".format(self.tag)


class Image(Tag):
    def __init__(self, name, src):
        super().__init__(name)
        self.tag = 'img'
        self.src = src

    def get_html(self):
        return "<{0} src='{1}'>".format(self.tag, self.src)


class Text(Tag):
    def __init__(self, name, content):
        super().__init__(name)
        self.tag = 'p'
        self.content = content

    def get_html(self):
        return "<{0}>{1}</{0}>".format(self.tag, self.content)


class Input(Tag):
    def __init__(self, name):
        super().__init__(name)
        self.tag = 'input'

    def get_html(self):
        return "<{0}></{0}>".format(self.tag)


class Link(Tag):
    def __init__(self, name, href, content):
        super().__init__(name)
        self.tag = 'a'
        self.href = href
        self.content = content

    def get_html(self):
        return "<{0} href='{1}'>{2}</{0}>".format(self.tag, self.href, self.content)



factory = TagFactory()
elements = ['image', 'p', 'a', 'input']
for el in elements:
    print(factory.create_tag(el).get_html())