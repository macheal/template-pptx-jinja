import jinja2


from template_pptx_jinja.render import PPTXRendering


def main():
    input_path = 'example/template.pptx'

    model = {
        "name": "John",
        "number": 3,
        "step": [
            {
                "name": "analysis"
            },
            {
                "name": "design"
            },
            {
                "name": "production"
            },
            {
                "name": "test"
            }
        ],
        "relationship_size": [{"name":"张三","size":"10"},{"name":"李四","size":"1000"},{"name":"王五","size":"2000"}]
    }
    pictures = {
        "p1": "example/image.jpg"
    }

    data = {
        'model': model,
        'pictures': pictures
    }

    def plural(input, word_ending):
        return word_ending if input > 0 else ''

    jinja2_env = jinja2.Environment()
    jinja2_env.filters['plural'] = plural

    output_path = 'example/presentation_generated.pptx'
    rendering = PPTXRendering(input_path, data, output_path, jinja2_env)
    message = rendering.process()
    print(message)

if __name__ == '__main__':
    main()
