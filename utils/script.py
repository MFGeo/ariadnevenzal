import os
import click

@click.command()
@click.option('--action', prompt=True)
@click.option('--path', default="", type=click.Path())
def run(action, path):
    click.echo(f"Proceeding to run script {action}")
    if action == "gallery-images":
        click.echo(f"Root path {path}")
        image_files = [f for f in os.listdir(path)]
        basename = os.path.basename(path)
        for image_file in image_files:
            click.echo(f"- image_path: gallery/archive/{basename}/{image_file}")
            click.echo(f"  caption: IMAGE TITLE")
            click.echo(f"  copyright: © Oscar Penelo")


if __name__ == '__main__':
    run()