class Main extends hxd.App {
    override function init() {
        super.init();
        var tf = new h2d.Text(hxd.res.DefaultFont.get(), s2d);
        tf.text = "LaserTank Extended POC";
    }
    static function main() {
        new Main();
    }
}