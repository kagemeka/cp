'use strict';
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var IO = /** @class */ (function () {
    function IO() {
        this.fs = require('fs');
        var fs = this.fs;
        var chunks = this.toChunks(this.readStdin());
        this.chunks = this.toGen(chunks);
    }
    IO.prototype.readStdin = function () {
        var fs = this.fs;
        return fs.readFileSync('/dev/stdin', 'utf8');
    };
    IO.prototype.toChunks = function (s) {
        return (s.trim().split(/ |\n/));
    };
    IO.prototype.toGen = function (chunks) {
        var _i, chunks_1, c;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _i = 0, chunks_1 = chunks;
                    _a.label = 1;
                case 1:
                    if (!(_i < chunks_1.length)) return [3 /*break*/, 4];
                    c = chunks_1[_i];
                    return [4 /*yield*/, c];
                case 2:
                    _a.sent();
                    _a.label = 3;
                case 3:
                    _i++;
                    return [3 /*break*/, 1];
                case 4: return [2 /*return*/];
            }
        });
    };
    IO.prototype.read = function () {
        return (this.chunks.next().value);
    };
    IO.prototype.readInt = function () {
        return +this.read();
    };
    return IO;
}());
var Solver = /** @class */ (function () {
    function Solver() {
        this.io = new IO();
    }
    Solver.prototype.run = function () {
        this.prepare();
        this.solve();
    };
    return Solver;
}());
var ABC001A = /** @class */ (function (_super) {
    __extends(ABC001A, _super);
    function ABC001A() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    ABC001A.prototype.prepare = function () {
        var io = this.io;
        var h1 = io.readInt();
        var h2 = io.readInt();
        this.h1 = h1;
        this.h2 = h2;
    };
    ABC001A.prototype.solve = function () {
        var h1 = this.h1;
        var h2 = this.h2;
        var d = h1 - h2;
        console.log(d);
    };
    return ABC001A;
}(Solver));
function main() {
    new ABC001A().run();
}
main();
