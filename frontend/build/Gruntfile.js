module.exports = function(grunt) {
    // Project configuration.
    grunt.initConfig({
        watch: {
            jst: {
                files: [
                    '../apps/**/*.html'
                ],
                tasks: ['jst']
            }
        },
        // Task configuration.
        jst: {
            compile: {
                options: {
                    processName: function(filename) {
                        //Shortens the file path for the template.
                        return filename.slice(filename.indexOf("templates")+10, filename.length).replace('.html','');
                    }
                },
                files: {
                    "../assets/templates.js": ["../apps/**/*.html"]
                }
            }
        },
    });

    // These plugins provide necessary tasks.
    grunt.loadNpmTasks('grunt-contrib-jst');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-processhtml');

    // Default task.
    grunt.registerTask('default', ['jst','watch']);
    grunt.registerTask('build', ['jst']);
};
