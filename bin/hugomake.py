from pathlib import Path


def main():
   this_file = Path(__file__)
   public_dir = this_file.parent.parent.joinpath('hugo-resources').joinpath('public')
   templates_dir = public_dir.joinpath('templates')
   if not templates_dir.exists():
      templates_dir.mkdir()

   new_index_file = public_dir.joinpath('index.html')

   index_file = templates_dir.joinpath('index.html')

   with new_index_file.open('r') as fr, index_file.open('w') as fw:
      html_content = fr.read()
      html_content = html_content.replace('="/', '="/static/')
      html_content = html_content.replace("images/author.jpg", "/static/images/author.jpg")
      fw.write(html_content)
   return 0


if __name__ == '__main__':
   exit(main())
